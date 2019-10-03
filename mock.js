var Mock = require('./mock-min.js');

function getMockData(data) {
    var mock = Mock.mock(JSON.parse(data));
    return  JSON.stringify(mock,null,4);
}