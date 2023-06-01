# recursive function gives map

import java.util.HashMap;

#
#import java.util.HashMap;

# public class Parser {
# 	private final static String NESTING_DELIMITER = "  ";  // 2 blank spaces
#
# 	public static HashMap<String, Object> parse(String input){
# 		HashMap<String, Object> map = new HashMap<String, Object>();
# 		if(input != null && input.length() != 0) {
# 			String[] lines = input.split("\n");
# 			int i, n = lines.length;
#
# 			for(i = 0; i < n; i++) {
# 				String[] parts = lines[i].split(":");
# 				if(parts.length == 1) {
# 					StringBuilder inner = new StringBuilder();
# 					++i;
#
# 					while(i < n) {
# 						if(lines[i].startsWith(NESTING_DELIMITER)) {
# 							inner.append(lines[i].substring(2));
# 							inner.append("\n");
# 						}else {
# 							break;
# 						}
#
# 						++i;
# 					}
#
# 					map.put(parts[0], parse(inner.toString()));
# 				}else {
# 					map.put(parts[0], parts[1]);
# 				}
# 			}
# 		}
#
# 		return map;
# 	}
# }
#