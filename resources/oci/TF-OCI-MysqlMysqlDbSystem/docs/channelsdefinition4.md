# TF::OCI::MysqlMysqlDbSystem ChannelsDefinition4

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
    "<a href="#sslcacertificate" title="SslCaCertificate">SslCaCertificate</a>" : <i>[ <a href="channelsdefinition3.md">ChannelsDefinition3</a>, ... ]</i>,
    "<a href="#sslmode" title="SslMode">SslMode</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
<a href="#sslcacertificate" title="SslCaCertificate">SslCaCertificate</a>: <i>
      - <a href="channelsdefinition3.md">ChannelsDefinition3</a></i>
<a href="#sslmode" title="SslMode">SslMode</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCaCertificate

_Required_: No

_Type_: List of <a href="channelsdefinition3.md">ChannelsDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

