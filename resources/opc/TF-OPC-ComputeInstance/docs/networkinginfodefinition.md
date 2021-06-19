# TF::OPC::ComputeInstance NetworkingInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dns" title="Dns">Dns</a>" : <i>[ String, ... ]</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#ipnetwork" title="IpNetwork">IpNetwork</a>" : <i>String</i>,
    "<a href="#isdefaultgateway" title="IsDefaultGateway">IsDefaultGateway</a>" : <i>Boolean</i>,
    "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
    "<a href="#nameservers" title="NameServers">NameServers</a>" : <i>[ String, ... ]</i>,
    "<a href="#nat" title="Nat">Nat</a>" : <i>[ String, ... ]</i>,
    "<a href="#searchdomains" title="SearchDomains">SearchDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#seclists" title="SecLists">SecLists</a>" : <i>[ String, ... ]</i>,
    "<a href="#sharednetwork" title="SharedNetwork">SharedNetwork</a>" : <i>Boolean</i>,
    "<a href="#vnic" title="Vnic">Vnic</a>" : <i>String</i>,
    "<a href="#vnicsets" title="VnicSets">VnicSets</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dns" title="Dns">Dns</a>: <i>
      - String</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#ipnetwork" title="IpNetwork">IpNetwork</a>: <i>String</i>
<a href="#isdefaultgateway" title="IsDefaultGateway">IsDefaultGateway</a>: <i>Boolean</i>
<a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
<a href="#nameservers" title="NameServers">NameServers</a>: <i>
      - String</i>
<a href="#nat" title="Nat">Nat</a>: <i>
      - String</i>
<a href="#searchdomains" title="SearchDomains">SearchDomains</a>: <i>
      - String</i>
<a href="#seclists" title="SecLists">SecLists</a>: <i>
      - String</i>
<a href="#sharednetwork" title="SharedNetwork">SharedNetwork</a>: <i>Boolean</i>
<a href="#vnic" title="Vnic">Vnic</a>: <i>String</i>
<a href="#vnicsets" title="VnicSets">VnicSets</a>: <i>
      - String</i>
</pre>

## Properties

#### Dns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefaultGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecLists

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vnic

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicSets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

