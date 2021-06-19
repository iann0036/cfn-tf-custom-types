# TF::FortiOS::SystemCsf FabricDeviceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesstoken" title="AccessToken">AccessToken</a>" : <i>String</i>,
    "<a href="#deviceip" title="DeviceIp">DeviceIp</a>" : <i>String</i>,
    "<a href="#devicetype" title="DeviceType">DeviceType</a>" : <i>String</i>,
    "<a href="#httpsport" title="HttpsPort">HttpsPort</a>" : <i>Double</i>,
    "<a href="#login" title="Login">Login</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesstoken" title="AccessToken">AccessToken</a>: <i>String</i>
<a href="#deviceip" title="DeviceIp">DeviceIp</a>: <i>String</i>
<a href="#devicetype" title="DeviceType">DeviceType</a>: <i>String</i>
<a href="#httpsport" title="HttpsPort">HttpsPort</a>: <i>Double</i>
<a href="#login" title="Login">Login</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
</pre>

## Properties

#### AccessToken

Device access token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceIp

Device IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceType

Device type. Valid values: `fortimail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsPort

HTTPS port for fabric device.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

Device login name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Device name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Device login password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

