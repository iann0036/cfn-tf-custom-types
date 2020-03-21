# Terraform::Panos::Telemetry

CloudFormation equivalent of panos_telemetry

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::Telemetry",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#applicationreports" title="ApplicationReports">ApplicationReports</a>" : <i>Boolean</i>,
        "<a href="#filetypeidentificationreports" title="FileTypeIdentificationReports">FileTypeIdentificationReports</a>" : <i>Boolean</i>,
        "<a href="#passivednsmonitoring" title="PassiveDnsMonitoring">PassiveDnsMonitoring</a>" : <i>Boolean</i>,
        "<a href="#productusagestats" title="ProductUsageStats">ProductUsageStats</a>" : <i>Boolean</i>,
        "<a href="#threatpreventiondata" title="ThreatPreventionData">ThreatPreventionData</a>" : <i>Boolean</i>,
        "<a href="#threatpreventionpacketcaptures" title="ThreatPreventionPacketCaptures">ThreatPreventionPacketCaptures</a>" : <i>Boolean</i>,
        "<a href="#threatpreventionreports" title="ThreatPreventionReports">ThreatPreventionReports</a>" : <i>Boolean</i>,
        "<a href="#urlreports" title="UrlReports">UrlReports</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::Telemetry
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#applicationreports" title="ApplicationReports">ApplicationReports</a>: <i>Boolean</i>
    <a href="#filetypeidentificationreports" title="FileTypeIdentificationReports">FileTypeIdentificationReports</a>: <i>Boolean</i>
    <a href="#passivednsmonitoring" title="PassiveDnsMonitoring">PassiveDnsMonitoring</a>: <i>Boolean</i>
    <a href="#productusagestats" title="ProductUsageStats">ProductUsageStats</a>: <i>Boolean</i>
    <a href="#threatpreventiondata" title="ThreatPreventionData">ThreatPreventionData</a>: <i>Boolean</i>
    <a href="#threatpreventionpacketcaptures" title="ThreatPreventionPacketCaptures">ThreatPreventionPacketCaptures</a>: <i>Boolean</i>
    <a href="#threatpreventionreports" title="ThreatPreventionReports">ThreatPreventionReports</a>: <i>Boolean</i>
    <a href="#urlreports" title="UrlReports">UrlReports</a>: <i>Boolean</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationReports

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTypeIdentificationReports

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveDnsMonitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductUsageStats

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPreventionData

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPreventionPacketCaptures

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPreventionReports

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlReports

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

