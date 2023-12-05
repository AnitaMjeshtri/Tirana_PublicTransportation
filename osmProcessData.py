import overpy
import json

api = overpy.Overpass()

node_ids = ["5295493338", "5295493339", "5295490950", "5295490951", "5295489890", "5295489891",
            "5295488398", "5295488399", "5295472690", "5295472691", "5295467531", "5295467532",
            "5295465143", "5295465144", "5295459710", "5295459711", "5295450787", "5295450788",
            "5295449526", "5295449527", "5295447187", "5295447188", "5295447190", "6177425345",
            "6236301260", "5295342516", "6324351044", "5295340332", "5295306493", "5295166851",
            "5295166852", "9850809599", "5295578677", "10148385134", "10148385136", "10148385135",
            "10916930182", "9850809599", "10148385134", "6327773232", "6030536786", "459205911",
            "674207428", "459205909", "173428835", "725194960", "587671422", "459205846", "459205848",
            "734623751", "459205833", "734631118", "459205831", "173428579",
            "459205837", "459205841", "674375275", "459205840", "469955584",
            "733056809", "675792897", "207183401", "469955585", "369730253",
            "229347215", "624093873", "173434427", "458859561", "551660469",
            "734635059", "457933451", "1207643109", "458516473", "1207642181",
            "670005932", "458718969", "458718972", "552713966", "552080449",
            "552713964", "458718965", "552713959", "547930052", "552713975",
            "552713974", "552713973", "1094515123", "552713958", "173207963",
            "458718975", "734857312", "458516622", "458363699", "552713982",
            "552713956", "552713981", "458359906", "659792481", "659792486",
            "659792485", "659792482", "552713989", "659792484", "458359905",
            "458359915", "458359916", "173207947", "624942244", "519024361",
            "547930053", "674412091", "519024365", "659804570", "676477790",
            "666112265", "676425796", "675320685", "675320687", "730038391",
            "675320688", "730204650", "730204649", "730204646", "256329289",
            "548092237", "675320691", "45316017", "256329294", "1109142293",
            "1109142294", "964244306", "1109142295", "548114871", "1193436003",
            "1199358210", "1193436007", "1199358211", "1193436008", "548126986",
            "729162837", "174150365", "729162836", "727525134", "727512015",
            "587671424", "727512013", "459205924", "459205921", "674207421",
            "459205914", "11197582396", "11197617966"
            ]

results = []
elDict = {}

for node_id in node_ids:
    result = api.query(f"node({node_id}); out body;")
    if result.nodes:
        node = result.nodes[0]

        lat = float(node.lat)
        lon = float(node.lon)

        elDict = {
            "type": "node",
            "id": node.id,
            "lat": lat,
            "lon": lon,
            "tags": {tag: str(node.tags[tag]) for tag in node.tags}
        }

    results.append(elDict)

file = open("Kombinat-Kinostudio.txt", "w")
json_result = json.dumps(results, indent=2)
file.write(json_result)
file.close()

print(json_result)