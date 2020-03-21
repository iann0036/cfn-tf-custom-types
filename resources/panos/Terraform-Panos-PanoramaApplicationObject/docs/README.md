# Terraform::Panos::PanoramaApplicationObject

CloudFormation equivalent of panos_panorama_application_object

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaApplicationObject",
    "Properties" : {
        "<a href="#abletofiletransfer" title="AbleToFileTransfer">AbleToFileTransfer</a>" : <i>Boolean</i>,
        "<a href="#algdisablecapability" title="AlgDisableCapability">AlgDisableCapability</a>" : <i>String</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#continuescanningforotherapplications" title="ContinueScanningForOtherApplications">ContinueScanningForOtherApplications</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#evasivebehavior" title="EvasiveBehavior">EvasiveBehavior</a>" : <i>Boolean</i>,
        "<a href="#excessivebandwidth" title="ExcessiveBandwidth">ExcessiveBandwidth</a>" : <i>Boolean</i>,
        "<a href="#hasknownvulnerability" title="HasKnownVulnerability">HasKnownVulnerability</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noappidcaching" title="NoAppIdCaching">NoAppIdCaching</a>" : <i>Boolean</i>,
        "<a href="#parentapp" title="ParentApp">ParentApp</a>" : <i>String</i>,
        "<a href="#pervasiveuse" title="PervasiveUse">PervasiveUse</a>" : <i>Boolean</i>,
        "<a href="#pronetomisuse" title="ProneToMisuse">ProneToMisuse</a>" : <i>Boolean</i>,
        "<a href="#risk" title="Risk">Risk</a>" : <i>Double</i>,
        "<a href="#subcategory" title="Subcategory">Subcategory</a>" : <i>String</i>,
        "<a href="#technology" title="Technology">Technology</a>" : <i>String</i>,
        "<a href="#tunnelsotherapplications" title="TunnelsOtherApplications">TunnelsOtherApplications</a>" : <i>Boolean</i>,
        "<a href="#usedbymalware" title="UsedByMalware">UsedByMalware</a>" : <i>Boolean</i>,
        "<a href="#defaults" title="Defaults">Defaults</a>" : <i>[ <a href="defaults.md">Defaults</a>, ... ]</i>,
        "<a href="#scanning" title="Scanning">Scanning</a>" : <i>[ <a href="scanning.md">Scanning</a>, ... ]</i>,
        "<a href="#timeoutsettings" title="TimeoutSettings">TimeoutSettings</a>" : <i>[ <a href="timeoutsettings.md">TimeoutSettings</a>, ... ]</i>,
        "<a href="#icmp" title="Icmp">Icmp</a>" : <i>[ <a href="icmp.md">Icmp</a>, ... ]</i>,
        "<a href="#icmp6" title="Icmp6">Icmp6</a>" : <i>[ <a href="icmp6.md">Icmp6</a>, ... ]</i>,
        "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>[ <a href="ipprotocol.md">IpProtocol</a>, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>[ <a href="port.md">Port</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaApplicationObject
Properties:
    <a href="#abletofiletransfer" title="AbleToFileTransfer">AbleToFileTransfer</a>: <i>Boolean</i>
    <a href="#algdisablecapability" title="AlgDisableCapability">AlgDisableCapability</a>: <i>String</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#continuescanningforotherapplications" title="ContinueScanningForOtherApplications">ContinueScanningForOtherApplications</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#evasivebehavior" title="EvasiveBehavior">EvasiveBehavior</a>: <i>Boolean</i>
    <a href="#excessivebandwidth" title="ExcessiveBandwidth">ExcessiveBandwidth</a>: <i>Boolean</i>
    <a href="#hasknownvulnerability" title="HasKnownVulnerability">HasKnownVulnerability</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noappidcaching" title="NoAppIdCaching">NoAppIdCaching</a>: <i>Boolean</i>
    <a href="#parentapp" title="ParentApp">ParentApp</a>: <i>String</i>
    <a href="#pervasiveuse" title="PervasiveUse">PervasiveUse</a>: <i>Boolean</i>
    <a href="#pronetomisuse" title="ProneToMisuse">ProneToMisuse</a>: <i>Boolean</i>
    <a href="#risk" title="Risk">Risk</a>: <i>Double</i>
    <a href="#subcategory" title="Subcategory">Subcategory</a>: <i>String</i>
    <a href="#technology" title="Technology">Technology</a>: <i>String</i>
    <a href="#tunnelsotherapplications" title="TunnelsOtherApplications">TunnelsOtherApplications</a>: <i>Boolean</i>
    <a href="#usedbymalware" title="UsedByMalware">UsedByMalware</a>: <i>Boolean</i>
    <a href="#defaults" title="Defaults">Defaults</a>: <i>
      - <a href="defaults.md">Defaults</a></i>
    <a href="#scanning" title="Scanning">Scanning</a>: <i>
      - <a href="scanning.md">Scanning</a></i>
    <a href="#timeoutsettings" title="TimeoutSettings">TimeoutSettings</a>: <i>
      - <a href="timeoutsettings.md">TimeoutSettings</a></i>
    <a href="#icmp" title="Icmp">Icmp</a>: <i>
      - <a href="icmp.md">Icmp</a></i>
    <a href="#icmp6" title="Icmp6">Icmp6</a>: <i>
      - <a href="icmp6.md">Icmp6</a></i>
    <a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>
      - <a href="ipprotocol.md">IpProtocol</a></i>
    <a href="#port" title="Port">Port</a>: <i>
      - <a href="port.md">Port</a></i>
</pre>

## Properties

#### AbleToFileTransfer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlgDisableCapability

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinueScanningForOtherApplications

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvasiveBehavior

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcessiveBandwidth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasKnownVulnerability

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAppIdCaching

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentApp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PervasiveUse

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProneToMisuse

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Risk

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subcategory

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Technology

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelsOtherApplications

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsedByMalware

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Defaults

_Required_: No

_Type_: List of <a href="defaults.md">Defaults</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scanning

_Required_: No

_Type_: List of <a href="scanning.md">Scanning</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSettings

_Required_: No

_Type_: List of <a href="timeoutsettings.md">TimeoutSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmp

_Required_: No

_Type_: List of <a href="icmp.md">Icmp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmp6

_Required_: No

_Type_: List of <a href="icmp6.md">Icmp6</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

_Required_: No

_Type_: List of <a href="ipprotocol.md">IpProtocol</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="port.md">Port</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

