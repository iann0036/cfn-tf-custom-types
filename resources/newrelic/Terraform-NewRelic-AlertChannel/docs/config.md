# Terraform::NewRelic::AlertChannel Config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
    "<a href="#authpassword" title="AuthPassword">AuthPassword</a>" : <i>String</i>,
    "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
    "<a href="#authusername" title="AuthUsername">AuthUsername</a>" : <i>String</i>,
    "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
    "<a href="#channel" title="Channel">Channel</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="config-headers.md">Headers</a>, ... ]</i>,
    "<a href="#headersstring" title="HeadersString">HeadersString</a>" : <i>String</i>,
    "<a href="#includejsonattachment" title="IncludeJsonAttachment">IncludeJsonAttachment</a>" : <i>String</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#payload" title="Payload">Payload</a>" : <i>[ <a href="config-payload.md">Payload</a>, ... ]</i>,
    "<a href="#payloadstring" title="PayloadString">PayloadString</a>" : <i>String</i>,
    "<a href="#payloadtype" title="PayloadType">PayloadType</a>" : <i>String</i>,
    "<a href="#recipients" title="Recipients">Recipients</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#routekey" title="RouteKey">RouteKey</a>" : <i>String</i>,
    "<a href="#servicekey" title="ServiceKey">ServiceKey</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>String</i>,
    "<a href="#teams" title="Teams">Teams</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
<a href="#authpassword" title="AuthPassword">AuthPassword</a>: <i>String</i>
<a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
<a href="#authusername" title="AuthUsername">AuthUsername</a>: <i>String</i>
<a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
<a href="#channel" title="Channel">Channel</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="config-headers.md">Headers</a></i>
<a href="#headersstring" title="HeadersString">HeadersString</a>: <i>String</i>
<a href="#includejsonattachment" title="IncludeJsonAttachment">IncludeJsonAttachment</a>: <i>String</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#payload" title="Payload">Payload</a>: <i>
      - <a href="config-payload.md">Payload</a></i>
<a href="#payloadstring" title="PayloadString">PayloadString</a>: <i>String</i>
<a href="#payloadtype" title="PayloadType">PayloadType</a>: <i>String</i>
<a href="#recipients" title="Recipients">Recipients</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#routekey" title="RouteKey">RouteKey</a>: <i>String</i>
<a href="#servicekey" title="ServiceKey">ServiceKey</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>String</i>
<a href="#teams" title="Teams">Teams</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#userid" title="UserId">UserId</a>: <i>String</i>
</pre>

## Properties

#### ApiKey

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthUsername

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseUrl

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Channel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No
_Type_: List of <a href="config-headers.md">Headers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadersString

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeJsonAttachment

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Payload

_Required_: No
_Type_: List of <a href="config-payload.md">Payload</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayloadString

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayloadType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteKey

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceKey

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

