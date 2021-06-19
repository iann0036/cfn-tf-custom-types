# TF::MSO::SchemaTemplateBd

CloudFormation equivalent of mso_schema_template_bd

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaTemplateBd",
    "Properties" : {
        "<a href="#dhcppolicy" title="DhcpPolicy">DhcpPolicy</a>" : <i>[ <a href="dhcppolicydefinition.md">DhcpPolicyDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#intersitebumtraffic" title="IntersiteBumTraffic">IntersiteBumTraffic</a>" : <i>Boolean</i>,
        "<a href="#layer2stretch" title="Layer2Stretch">Layer2Stretch</a>" : <i>Boolean</i>,
        "<a href="#layer2unknownunicast" title="Layer2UnknownUnicast">Layer2UnknownUnicast</a>" : <i>String</i>,
        "<a href="#layer3multicast" title="Layer3Multicast">Layer3Multicast</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#optimizewanbandwidth" title="OptimizeWanBandwidth">OptimizeWanBandwidth</a>" : <i>Boolean</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#vrfname" title="VrfName">VrfName</a>" : <i>String</i>,
        "<a href="#vrfschemaid" title="VrfSchemaId">VrfSchemaId</a>" : <i>String</i>,
        "<a href="#vrftemplatename" title="VrfTemplateName">VrfTemplateName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaTemplateBd
Properties:
    <a href="#dhcppolicy" title="DhcpPolicy">DhcpPolicy</a>: <i>
      - <a href="dhcppolicydefinition.md">DhcpPolicyDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#intersitebumtraffic" title="IntersiteBumTraffic">IntersiteBumTraffic</a>: <i>Boolean</i>
    <a href="#layer2stretch" title="Layer2Stretch">Layer2Stretch</a>: <i>Boolean</i>
    <a href="#layer2unknownunicast" title="Layer2UnknownUnicast">Layer2UnknownUnicast</a>: <i>String</i>
    <a href="#layer3multicast" title="Layer3Multicast">Layer3Multicast</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#optimizewanbandwidth" title="OptimizeWanBandwidth">OptimizeWanBandwidth</a>: <i>Boolean</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#vrfname" title="VrfName">VrfName</a>: <i>String</i>
    <a href="#vrfschemaid" title="VrfSchemaId">VrfSchemaId</a>: <i>String</i>
    <a href="#vrftemplatename" title="VrfTemplateName">VrfTemplateName</a>: <i>String</i>
</pre>

## Properties

#### DhcpPolicy

_Required_: No

_Type_: List of <a href="dhcppolicydefinition.md">DhcpPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntersiteBumTraffic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer2Stretch

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer2UnknownUnicast

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer3Multicast

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizeWanBandwidth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfSchemaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfTemplateName

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

