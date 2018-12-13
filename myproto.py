myproto_protocol = Proto("MyProto",  "Test Protocol")

myproto_protocol.fields = {}

function myproto_protocol.dissector(buffer, pinfo, tree)
  length = buffer:len()
  if length == 0 then return end

  pinfo.cols.protocol = myproto_protocol.name

  local subtree = tree:add(myproto_protocol, buffer(), "Test Protocol Data")
end

local tcp_port = DissectorTable.get("tcp.port")
tcp_port:add(54845, myproto_protocol)