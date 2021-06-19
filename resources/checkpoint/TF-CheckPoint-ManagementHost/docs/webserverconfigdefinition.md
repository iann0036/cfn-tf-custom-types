# TF::CheckPoint::ManagementHost WebServerConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalports" title="AdditionalPorts">AdditionalPorts</a>" : <i>[ String, ... ]</i>,
    "<a href="#applicationengines" title="ApplicationEngines">ApplicationEngines</a>" : <i>[ String, ... ]</i>,
    "<a href="#listenstandardport" title="ListenStandardPort">ListenStandardPort</a>" : <i>Boolean</i>,
    "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
    "<a href="#protectedby" title="ProtectedBy">ProtectedBy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#additionalports" title="AdditionalPorts">AdditionalPorts</a>: <i>
      - String</i>
<a href="#applicationengines" title="ApplicationEngines">ApplicationEngines</a>: <i>
      - String</i>
<a href="#listenstandardport" title="ListenStandardPort">ListenStandardPort</a>: <i>Boolean</i>
<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
<a href="#protectedby" title="ProtectedBy">ProtectedBy</a>: <i>String</i>
</pre>

## Properties

#### AdditionalPorts

Server additional ports.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationEngines

Application engines of this web server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenStandardPort

"Whether server listens to standard port.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

Operating System.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectedBy

Network object which protects this server identified by the name or UID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

