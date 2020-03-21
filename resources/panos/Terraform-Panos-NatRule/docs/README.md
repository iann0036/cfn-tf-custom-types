# Terraform::Panos::NatRule

CloudFormation equivalent of panos_nat_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::NatRule",
    "Properties" : {
        "<a href="#dataddress" title="DatAddress">DatAddress</a>" : <i>String</i>,
        "<a href="#datdynamicdistribution" title="DatDynamicDistribution">DatDynamicDistribution</a>" : <i>String</i>,
        "<a href="#datport" title="DatPort">DatPort</a>" : <i>Double</i>,
        "<a href="#dattype" title="DatType">DatType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationzone" title="DestinationZone">DestinationZone</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rulebase" title="Rulebase">Rulebase</a>" : <i>String</i>,
        "<a href="#sataddresstype" title="SatAddressType">SatAddressType</a>" : <i>String</i>,
        "<a href="#satfallbackinterface" title="SatFallbackInterface">SatFallbackInterface</a>" : <i>String</i>,
        "<a href="#satfallbackipaddress" title="SatFallbackIpAddress">SatFallbackIpAddress</a>" : <i>String</i>,
        "<a href="#satfallbackiptype" title="SatFallbackIpType">SatFallbackIpType</a>" : <i>String</i>,
        "<a href="#satfallbacktranslatedaddresses" title="SatFallbackTranslatedAddresses">SatFallbackTranslatedAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#satfallbacktype" title="SatFallbackType">SatFallbackType</a>" : <i>String</i>,
        "<a href="#satinterface" title="SatInterface">SatInterface</a>" : <i>String</i>,
        "<a href="#satipaddress" title="SatIpAddress">SatIpAddress</a>" : <i>String</i>,
        "<a href="#satstaticbidirectional" title="SatStaticBiDirectional">SatStaticBiDirectional</a>" : <i>Boolean</i>,
        "<a href="#satstatictranslatedaddress" title="SatStaticTranslatedAddress">SatStaticTranslatedAddress</a>" : <i>String</i>,
        "<a href="#sattranslatedaddresses" title="SatTranslatedAddresses">SatTranslatedAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#sattype" title="SatType">SatType</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcezones" title="SourceZones">SourceZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#tointerface" title="ToInterface">ToInterface</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::NatRule
Properties:
    <a href="#dataddress" title="DatAddress">DatAddress</a>: <i>String</i>
    <a href="#datdynamicdistribution" title="DatDynamicDistribution">DatDynamicDistribution</a>: <i>String</i>
    <a href="#datport" title="DatPort">DatPort</a>: <i>Double</i>
    <a href="#dattype" title="DatType">DatType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>: <i>
      - String</i>
    <a href="#destinationzone" title="DestinationZone">DestinationZone</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rulebase" title="Rulebase">Rulebase</a>: <i>String</i>
    <a href="#sataddresstype" title="SatAddressType">SatAddressType</a>: <i>String</i>
    <a href="#satfallbackinterface" title="SatFallbackInterface">SatFallbackInterface</a>: <i>String</i>
    <a href="#satfallbackipaddress" title="SatFallbackIpAddress">SatFallbackIpAddress</a>: <i>String</i>
    <a href="#satfallbackiptype" title="SatFallbackIpType">SatFallbackIpType</a>: <i>String</i>
    <a href="#satfallbacktranslatedaddresses" title="SatFallbackTranslatedAddresses">SatFallbackTranslatedAddresses</a>: <i>
      - String</i>
    <a href="#satfallbacktype" title="SatFallbackType">SatFallbackType</a>: <i>String</i>
    <a href="#satinterface" title="SatInterface">SatInterface</a>: <i>String</i>
    <a href="#satipaddress" title="SatIpAddress">SatIpAddress</a>: <i>String</i>
    <a href="#satstaticbidirectional" title="SatStaticBiDirectional">SatStaticBiDirectional</a>: <i>Boolean</i>
    <a href="#satstatictranslatedaddress" title="SatStaticTranslatedAddress">SatStaticTranslatedAddress</a>: <i>String</i>
    <a href="#sattranslatedaddresses" title="SatTranslatedAddresses">SatTranslatedAddresses</a>: <i>
      - String</i>
    <a href="#sattype" title="SatType">SatType</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
    <a href="#sourcezones" title="SourceZones">SourceZones</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#tointerface" title="ToInterface">ToInterface</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
</pre>

## Properties

#### DatAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatDynamicDistribution

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddresses

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rulebase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatAddressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackIpType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackTranslatedAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatStaticBiDirectional

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatStaticTranslatedAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatTranslatedAddresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceZones

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

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

