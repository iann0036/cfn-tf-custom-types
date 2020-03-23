# Terraform::AWS::StoragegatewayGateway

Manages an AWS Storage Gateway file, tape, or volume gateway in the provider region.

~> NOTE: The Storage Gateway API requires the gateway to be connected to properly return information after activation. If you are receiving `The specified gateway is not connected` errors during resource creation (gateway activation), ensure your gateway instance meets the [Storage Gateway requirements](https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html).

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

Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLogGroupArn

The Amazon Resource Name (ARN) of the Amazon CloudWatch log group to use to monitor and log events in the gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIpAddress

Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayName

Name of the gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayTimezone

Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayType

Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediumChangerType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmbGuestPassword

Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. Terraform can only detect drift of the existence of a guest password, not its actual value from the gateway. Terraform can however update the password with changing the argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TapeDriveType

Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

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

