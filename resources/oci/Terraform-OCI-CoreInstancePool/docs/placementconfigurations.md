# Terraform::OCI::CoreInstancePool PlacementConfigurations

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
    "<a href="#faultdomains" title="FaultDomains">FaultDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#primarysubnetid" title="PrimarySubnetId">PrimarySubnetId</a>" : <i>String</i>,
    "<a href="#secondaryvnicsubnets" title="SecondaryVnicSubnets">SecondaryVnicSubnets</a>" : <i>[ <a href="placementconfigurations-secondaryvnicsubnets.md">SecondaryVnicSubnets</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
<a href="#faultdomains" title="FaultDomains">FaultDomains</a>: <i>
      - String</i>
<a href="#primarysubnetid" title="PrimarySubnetId">PrimarySubnetId</a>: <i>String</i>
<a href="#secondaryvnicsubnets" title="SecondaryVnicSubnets">SecondaryVnicSubnets</a>: <i>
      - <a href="placementconfigurations-secondaryvnicsubnets.md">SecondaryVnicSubnets</a></i>
</pre>

## Properties

#### AvailabilityDomain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimarySubnetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryVnicSubnets

_Required_: No

_Type_: List of <a href="placementconfigurations-secondaryvnicsubnets.md">SecondaryVnicSubnets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

