var Mock = require('mockjs');

function getMockData(data) {
    var mock = Mock.mock(JSON.parse(data));
    return  JSON.stringify(mock,null,4);
}