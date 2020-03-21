# Terraform::Panos::Telemetry

This resource allows you to add/update/delete telemetry sharing.

Join other Palo Alto Networks customers in a global sharing community, helping
to raise the bar against the latest attack techniques. Your participation
allows us to deliver new threat prevention controls across the attack
lifecycle. Choose the type of data you share across applications, threat
intelligence, and device health information to improve the fidelity of the
protections we deliver. This is an opt-in feature controlled with granular
policy, and we encourage you to join the community.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::Telemetry",
    "Properties" : {
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

#### ApplicationReports

Application reports.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTypeIdentificationReports

File type identification
reports.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveDnsMonitoring

Passive DNS monitoring.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductUsageStats

Health and performance reports.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPreventionData

Threat prevention data.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPreventionPacketCaptures

Enable sending packet-
captures with threat prevention information. This requires that
`threat_prevention_data` also be enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPreventionReports

Threat reports.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlReports

URL reports.

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

