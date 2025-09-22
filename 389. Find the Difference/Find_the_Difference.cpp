class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char,int> sMap;
        map<char,int> tMap;
        for(auto &e : s){
            ++sMap[e];
        }
        for(auto &e : t){
            ++tMap[e];
        }
        for(auto &e : tMap){
            auto itSmap = sMap.find(e.first);
            if (e.second != itSmap->second || itSmap == sMap.end()){
                return e.first;
            }
        }
        return '\0';
    }
};