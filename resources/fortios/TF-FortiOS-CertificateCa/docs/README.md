# TF::FortiOS::CertificateCa

CA certificate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::CertificateCa",
    "Properties" : {
        "<a href="#autoupdatedays" title="AutoUpdateDays">AutoUpdateDays</a>" : <i>Double</i>,
        "<a href="#autoupdatedayswarning" title="AutoUpdateDaysWarning">AutoUpdateDaysWarning</a>" : <i>Double</i>,
        "<a href="#ca" title="Ca">Ca</a>" : <i>String</i>,
        "<a href="#lastupdated" title="LastUpdated">LastUpdated</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#range" title="Range">Range</a>" : <i>String</i>,
        "<a href="#scepurl" title="ScepUrl">ScepUrl</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#sslinspectiontrusted" title="SslInspectionTrusted">SslInspectionTrusted</a>" : <i>String</i>,
        "<a href="#trusted" title="Trusted">Trusted</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::CertificateCa
Properties:
    <a href="#autoupdatedays" title="AutoUpdateDays">AutoUpdateDays</a>: <i>Double</i>
    <a href="#autoupdatedayswarning" title="AutoUpdateDaysWarning">AutoUpdateDaysWarning</a>: <i>Double</i>
    <a href="#ca" title="Ca">Ca</a>: <i>String</i>
    <a href="#lastupdated" title="LastUpdated">LastUpdated</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#range" title="Range">Range</a>: <i>String</i>
    <a href="#scepurl" title="ScepUrl">ScepUrl</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#sslinspectiontrusted" title="SslInspectionTrusted">SslInspectionTrusted</a>: <i>String</i>
    <a href="#trusted" title="Trusted">Trusted</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AutoUpdateDays

Number of days to wait before requesting an updated CA certificate (0 - 4294967295, 0 = disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoUpdateDaysWarning

Number of days before an expiry-warning message is generated (0 - 4294967295, 0 = disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ca

CA certificate as a PEM file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdated

Time at which CA was last updated.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

Either global or VDOM IP address range for the CA certificate. Valid values: `global`, `vdom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScepUrl

URL of the SCEP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

CA certificate source type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP address for communications to the SCEP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslInspectionTrusted

Enable/disable this CA as a trusted CA for SSL inspection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusted

Enable/disable as a trusted CA. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

