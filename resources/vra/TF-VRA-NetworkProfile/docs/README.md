# TF::VRA::NetworkProfile

CloudFormation equivalent of vra_network_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::NetworkProfile",
    "Properties" : {
        "<a href="#customproperties" title="CustomProperties">CustomProperties</a>" : <i>[ <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fabricnetworkids" title="FabricNetworkIds">FabricNetworkIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#isolatedexternalfabricnetworkid" title="IsolatedExternalFabricNetworkId">IsolatedExternalFabricNetworkId</a>" : <i>String</i>,
        "<a href="#isolatednetworkcidrprefix" title="IsolatedNetworkCidrPrefix">IsolatedNetworkCidrPrefix</a>" : <i>Double</i>,
        "<a href="#isolatednetworkdomaincidr" title="IsolatedNetworkDomainCidr">IsolatedNetworkDomainCidr</a>" : <i>String</i>,
        "<a href="#isolatednetworkdomainid" title="IsolatedNetworkDomainId">IsolatedNetworkDomainId</a>" : <i>String</i>,
        "<a href="#isolationtype" title="IsolationType">IsolationType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#regionid" title="RegionId">RegionId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::NetworkProfile
Properties:
    <a href="#customproperties" title="CustomProperties">CustomProperties</a>: <i>
      - <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fabricnetworkids" title="FabricNetworkIds">FabricNetworkIds</a>: <i>
      - String</i>
    <a href="#isolatedexternalfabricnetworkid" title="IsolatedExternalFabricNetworkId">IsolatedExternalFabricNetworkId</a>: <i>String</i>
    <a href="#isolatednetworkcidrprefix" title="IsolatedNetworkCidrPrefix">IsolatedNetworkCidrPrefix</a>: <i>Double</i>
    <a href="#isolatednetworkdomaincidr" title="IsolatedNetworkDomainCidr">IsolatedNetworkDomainCidr</a>: <i>String</i>
    <a href="#isolatednetworkdomainid" title="IsolatedNetworkDomainId">IsolatedNetworkDomainId</a>: <i>String</i>
    <a href="#isolationtype" title="IsolationType">IsolationType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#regionid" title="RegionId">RegionId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### CustomProperties

Additional properties that may be used to extend the Network Profile object that is produced from this specification. For isolationType security group, datastoreId identifies the Compute Resource Edge datastore. computeCluster and resourcePoolId identify the Compute Resource Edge cluster. For isolationType subnet, distributedLogicalRouterStateLink identifies the on-demand network distributed local router. onDemandNetworkIPAssignmentType identifies the on-demand network IP range assignment type static, dynamic, or mixed.

_Required_: No

_Type_: List of <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricNetworkIds

A list of fabric network Ids which are assigned to the network profile.
example:[ "6543" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolatedExternalFabricNetworkId

The id of the fabric network used for outbound access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolatedNetworkCidrPrefix

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolatedNetworkDomainCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolatedNetworkDomainId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human-friendly name used as an identifier in APIs that support this option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionId

The id of the region for which this profile is defined as in vRealize Automation(vRA).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudAccountId

Returns the <code>CloudAccountId</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### ExternalRegionId

Returns the <code>ExternalRegionId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Links

Returns the <code>Links</code> value.

#### OrgId

Returns the <code>OrgId</code> value.

#### OrganizationId

Returns the <code>OrganizationId</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

