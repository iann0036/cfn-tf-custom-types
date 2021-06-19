# TF::MSO::SchemaSiteVrfRegion

CloudFormation equivalent of mso_schema_site_vrf_region

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MSO::SchemaSiteVrfRegion",
    "Properties" : {
        "<a href="#hubnetwork" title="HubNetwork">HubNetwork</a>" : <i>[ <a href="hubnetworkdefinition.md">HubNetworkDefinition</a>, ... ]</i>,
        "<a href="#hubnetworkenable" title="HubNetworkEnable">HubNetworkEnable</a>" : <i>Boolean</i>,
        "<a href="#regionname" title="RegionName">RegionName</a>" : <i>String</i>,
        "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
        "<a href="#siteid" title="SiteId">SiteId</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#vpngateway" title="VpnGateway">VpnGateway</a>" : <i>Boolean</i>,
        "<a href="#vrfname" title="VrfName">VrfName</a>" : <i>String</i>,
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>[ <a href="cidrdefinition.md">CidrDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MSO::SchemaSiteVrfRegion
Properties:
    <a href="#hubnetwork" title="HubNetwork">HubNetwork</a>: <i>
      - <a href="hubnetworkdefinition.md">HubNetworkDefinition</a></i>
    <a href="#hubnetworkenable" title="HubNetworkEnable">HubNetworkEnable</a>: <i>Boolean</i>
    <a href="#regionname" title="RegionName">RegionName</a>: <i>String</i>
    <a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
    <a href="#siteid" title="SiteId">SiteId</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#vpngateway" title="VpnGateway">VpnGateway</a>: <i>Boolean</i>
    <a href="#vrfname" title="VrfName">VrfName</a>: <i>String</i>
    <a href="#cidr" title="Cidr">Cidr</a>: <i>
      - <a href="cidrdefinition.md">CidrDefinition</a></i>
</pre>

## Properties

#### HubNetwork

_Required_: No

_Type_: List of <a href="hubnetworkdefinition.md">HubNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HubNetworkEnable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionName

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

#### TemplateName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cidr

_Required_: No

_Type_: List of <a href="cidrdefinition.md">CidrDefinition</a>

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

