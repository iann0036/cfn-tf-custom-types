# TF::MSO::SchemaSiteAnpEpgDomain

CloudFormation equivalent of mso_schema_site_anp_epg_domain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaSiteAnpEpgDomain",
    "Properties" : {
        "<a href="#allowmicrosegmentation" title="AllowMicroSegmentation">AllowMicroSegmentation</a>" : <i>Boolean</i>,
        "<a href="#anpname" title="AnpName">AnpName</a>" : <i>String</i>,
        "<a href="#deployimmediacy" title="DeployImmediacy">DeployImmediacy</a>" : <i>String</i>,
        "<a href="#dn" title="Dn">Dn</a>" : <i>String</i>,
        "<a href="#domaintype" title="DomainType">DomainType</a>" : <i>String</i>,
        "<a href="#enhancedlagpolicydn" title="EnhancedLagPolicyDn">EnhancedLagPolicyDn</a>" : <i>String</i>,
        "<a href="#enhancedlagpolicyname" title="EnhancedLagPolicyName">EnhancedLagPolicyName</a>" : <i>String</i>,
        "<a href="#epgname" title="EpgName">EpgName</a>" : <i>String</i>,
        "<a href="#microsegvlan" title="MicroSegVlan">MicroSegVlan</a>" : <i>Double</i>,
        "<a href="#microsegvlantype" title="MicroSegVlanType">MicroSegVlanType</a>" : <i>String</i>,
        "<a href="#portencapvlan" title="PortEncapVlan">PortEncapVlan</a>" : <i>Double</i>,
        "<a href="#portencapvlantype" title="PortEncapVlanType">PortEncapVlanType</a>" : <i>String</i>,
        "<a href="#resolutionimmediacy" title="ResolutionImmediacy">ResolutionImmediacy</a>" : <i>String</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#siteid" title="SiteId">SiteId</a>" : <i>String</i>,
        "<a href="#switchtype" title="SwitchType">SwitchType</a>" : <i>String</i>,
        "<a href="#switchingmode" title="SwitchingMode">SwitchingMode</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#vlanencapmode" title="VlanEncapMode">VlanEncapMode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaSiteAnpEpgDomain
Properties:
    <a href="#allowmicrosegmentation" title="AllowMicroSegmentation">AllowMicroSegmentation</a>: <i>Boolean</i>
    <a href="#anpname" title="AnpName">AnpName</a>: <i>String</i>
    <a href="#deployimmediacy" title="DeployImmediacy">DeployImmediacy</a>: <i>String</i>
    <a href="#dn" title="Dn">Dn</a>: <i>String</i>
    <a href="#domaintype" title="DomainType">DomainType</a>: <i>String</i>
    <a href="#enhancedlagpolicydn" title="EnhancedLagPolicyDn">EnhancedLagPolicyDn</a>: <i>String</i>
    <a href="#enhancedlagpolicyname" title="EnhancedLagPolicyName">EnhancedLagPolicyName</a>: <i>String</i>
    <a href="#epgname" title="EpgName">EpgName</a>: <i>String</i>
    <a href="#microsegvlan" title="MicroSegVlan">MicroSegVlan</a>: <i>Double</i>
    <a href="#microsegvlantype" title="MicroSegVlanType">MicroSegVlanType</a>: <i>String</i>
    <a href="#portencapvlan" title="PortEncapVlan">PortEncapVlan</a>: <i>Double</i>
    <a href="#portencapvlantype" title="PortEncapVlanType">PortEncapVlanType</a>: <i>String</i>
    <a href="#resolutionimmediacy" title="ResolutionImmediacy">ResolutionImmediacy</a>: <i>String</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#siteid" title="SiteId">SiteId</a>: <i>String</i>
    <a href="#switchtype" title="SwitchType">SwitchType</a>: <i>String</i>
    <a href="#switchingmode" title="SwitchingMode">SwitchingMode</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#vlanencapmode" title="VlanEncapMode">VlanEncapMode</a>: <i>String</i>
</pre>

## Properties

#### AllowMicroSegmentation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnpName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployImmediacy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedLagPolicyDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedLagPolicyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpgName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicroSegVlan

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicroSegVlanType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortEncapVlan

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortEncapVlanType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolutionImmediacy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanEncapMode

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

