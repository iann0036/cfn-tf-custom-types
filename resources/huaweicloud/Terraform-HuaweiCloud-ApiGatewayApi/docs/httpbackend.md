# Terraform::HuaweiCloud::ApiGatewayApi HttpBackend

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
    "<a href="#urldomain" title="UrlDomain">UrlDomain</a>" : <i>String</i>,
    "<a href="#vpcchannel" title="VpcChannel">VpcChannel</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
<a href="#urldomain" title="UrlDomain">UrlDomain</a>: <i>String</i>
<a href="#vpcchannel" title="VpcChannel">VpcChannel</a>: <i>String</i>
</pre>

## Properties

#### Method

Specifies the backend request method, including 'GET','POST','PUT' and etc..

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Specifies the backend request protocol. The value can be 'HTTP' and 'HTTPS'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout duration (in ms) for API Gateway to request for the backend service. Defaults to 50000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

Specifies the backend request path. The value must comply with URI specifications.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlDomain

Specifies the backend service address. An endpoint URL is in the format of
"domain name (or IP address):port number", with up to 255 characters. This parameter and `vpc_channel` are alternative.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcChannel

Specifies the VPC channel ID. This parameter and `url_domain` are alternative.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

