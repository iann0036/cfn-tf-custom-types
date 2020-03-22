# Terraform::AWS::StoragegatewayGateway

CloudFormation equivalent of aws_storagegateway_gateway

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::StoragegatewayGateway",
    "Properties" : {
        "<a href="#activationkey" title="ActivationKey">ActivationKey</a>" : <i>String</i>,
        "<a href="#cloudwatchloggrouparn" title="CloudwatchLogGroupArn">CloudwatchLogGroupArn</a>" : <i>String</i>,
        "<a href="#gatewayipaddress" title="GatewayIpAddress">GatewayIpAddress</a>" : <i>String</i>,
        "<a href="#gatewayname" title="GatewayName">GatewayName</a>" : <i>String</i>,
        "<a href="#gatewaytimezone" title="GatewayTimezone">GatewayTimezone</a>" : <i>String</i>,
        "<a href="#gatewaytype" title="GatewayType">GatewayType</a>" : <i>String</i>,
        "<a href="#mediumchangertype" title="MediumChangerType">MediumChangerType</a>" : <i>String</i>,
        "<a href="#smbguestpassword" title="SmbGuestPassword">SmbGuestPassword</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#tapedrivetype" title="TapeDriveType">TapeDriveType</a>" : <i>String</i>,
        "<a href="#smbactivedirectorysettings" title="SmbActiveDirectorySettings">SmbActiveDirectorySettings</a>" : <i>[ <a href="smbactivedirectorysettings.md">SmbActiveDirectorySettings</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::StoragegatewayGateway
Properties:
    <a href="#activationkey" title="ActivationKey">ActivationKey</a>: <i>String</i>
    <a href="#cloudwatchloggrouparn" title="CloudwatchLogGroupArn">CloudwatchLogGroupArn</a>: <i>String</i>
    <a href="#gatewayipaddress" title="GatewayIpAddress">GatewayIpAddress</a>: <i>String</i>
    <a href="#gatewayname" title="GatewayName">GatewayName</a>: <i>String</i>
    <a href="#gatewaytimezone" title="GatewayTimezone">GatewayTimezone</a>: <i>String</i>
    <a href="#gatewaytype" title="GatewayType">GatewayType</a>: <i>String</i>
    <a href="#mediumchangertype" title="MediumChangerType">MediumChangerType</a>: <i>String</i>
    <a href="#smbguestpassword" title="SmbGuestPassword">SmbGuestPassword</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#tapedrivetype" title="TapeDriveType">TapeDriveType</a>: <i>String</i>
    <a href="#smbactivedirectorysettings" title="SmbActiveDirectorySettings">SmbActiveDirectorySettings</a>: <i>
      - <a href="smbactivedirectorysettings.md">SmbActiveDirectorySettings</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ActivationKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLogGroupArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayTimezone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediumChangerType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmbGuestPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TapeDriveType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmbActiveDirectorySettings

_Required_: No

_Type_: List of <a href="smbactivedirectorysettings.md">SmbActiveDirectorySettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### GatewayId

Returns the <code>GatewayId</code> value.

#### Id

Returns the <code>Id</code> value.

