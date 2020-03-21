# Terraform::OpenTelekomCloud::WafDomainV1 Server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#backprotocol" title="BackProtocol">BackProtocol</a>" : <i>String</i>,
    "<a href="#frontprotocol" title="FrontProtocol">FrontProtocol</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#backprotocol" title="BackProtocol">BackProtocol</a>: <i>String</i>
<a href="#frontprotocol" title="FrontProtocol">FrontProtocol</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
</pre>

## Properties

#### Address

IP address or domain name of the web server that the client accesses. For example, 192.168.1.1 or www.a.com.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackProtocol

Protocl used by WAF to forward client requests to the server. The options are HTTP and HTTPS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontProtocol

Protocol type of the client. The options are HTTP and HTTPS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port number used by the web server. The value ranges from 0 to 65535, for example, 8080.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

