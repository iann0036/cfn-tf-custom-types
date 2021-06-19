# TF::Nutanix::Project

Provides a Nutanix Project resource to Create a Project.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nutanix::Project",
    "Properties" : {
        "<a href="#apiversion" title="ApiVersion">ApiVersion</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>, ... ]</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>, ... ]</i>,
        "<a href="#accountreferencelist" title="AccountReferenceList">AccountReferenceList</a>" : <i>[ <a href="accountreferencelistdefinition.md">AccountReferenceListDefinition</a>, ... ]</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>,
        "<a href="#defaultsubnetreference" title="DefaultSubnetReference">DefaultSubnetReference</a>" : <i>[ <a href="defaultsubnetreferencedefinition.md">DefaultSubnetReferenceDefinition</a>, ... ]</i>,
        "<a href="#environmentreferencelist" title="EnvironmentReferenceList">EnvironmentReferenceList</a>" : <i>[ <a href="environmentreferencelistdefinition.md">EnvironmentReferenceListDefinition</a>, ... ]</i>,
        "<a href="#externalnetworklist" title="ExternalNetworkList">ExternalNetworkList</a>" : <i>[ <a href="externalnetworklistdefinition.md">ExternalNetworkListDefinition</a>, ... ]</i>,
        "<a href="#externalusergroupreferencelist" title="ExternalUserGroupReferenceList">ExternalUserGroupReferenceList</a>" : <i>[ <a href="externalusergroupreferencelistdefinition.md">ExternalUserGroupReferenceListDefinition</a>, ... ]</i>,
        "<a href="#resourcedomain" title="ResourceDomain">ResourceDomain</a>" : <i>[ <a href="resourcedomaindefinition.md">ResourceDomainDefinition</a>, ... ]</i>,
        "<a href="#subnetreferencelist" title="SubnetReferenceList">SubnetReferenceList</a>" : <i>[ <a href="subnetreferencelistdefinition.md">SubnetReferenceListDefinition</a>, ... ]</i>,
        "<a href="#userreferencelist" title="UserReferenceList">UserReferenceList</a>" : <i>[ <a href="userreferencelistdefinition.md">UserReferenceListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nutanix::Project
Properties:
    <a href="#apiversion" title="ApiVersion">ApiVersion</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a></i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a></i>
    <a href="#accountreferencelist" title="AccountReferenceList">AccountReferenceList</a>: <i>
      - <a href="accountreferencelistdefinition.md">AccountReferenceListDefinition</a></i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
    <a href="#defaultsubnetreference" title="DefaultSubnetReference">DefaultSubnetReference</a>: <i>
      - <a href="defaultsubnetreferencedefinition.md">DefaultSubnetReferenceDefinition</a></i>
    <a href="#environmentreferencelist" title="EnvironmentReferenceList">EnvironmentReferenceList</a>: <i>
      - <a href="environmentreferencelistdefinition.md">EnvironmentReferenceListDefinition</a></i>
    <a href="#externalnetworklist" title="ExternalNetworkList">ExternalNetworkList</a>: <i>
      - <a href="externalnetworklistdefinition.md">ExternalNetworkListDefinition</a></i>
    <a href="#externalusergroupreferencelist" title="ExternalUserGroupReferenceList">ExternalUserGroupReferenceList</a>: <i>
      - <a href="externalusergroupreferencelistdefinition.md">ExternalUserGroupReferenceListDefinition</a></i>
    <a href="#resourcedomain" title="ResourceDomain">ResourceDomain</a>: <i>
      - <a href="resourcedomaindefinition.md">ResourceDomainDefinition</a></i>
    <a href="#subnetreferencelist" title="SubnetReferenceList">SubnetReferenceList</a>: <i>
      - <a href="subnetreferencelistdefinition.md">SubnetReferenceListDefinition</a></i>
    <a href="#userreferencelist" title="UserReferenceList">UserReferenceList</a>: <i>
      - <a href="userreferencelistdefinition.md">UserReferenceListDefinition</a></i>
</pre>

## Properties

#### ApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountReferenceList

_Required_: No

_Type_: List of <a href="accountreferencelistdefinition.md">AccountReferenceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSubnetReference

_Required_: No

_Type_: List of <a href="defaultsubnetreferencedefinition.md">DefaultSubnetReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentReferenceList

_Required_: No

_Type_: List of <a href="environmentreferencelistdefinition.md">EnvironmentReferenceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetworkList

_Required_: No

_Type_: List of <a href="externalnetworklistdefinition.md">ExternalNetworkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalUserGroupReferenceList

_Required_: No

_Type_: List of <a href="externalusergroupreferencelistdefinition.md">ExternalUserGroupReferenceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceDomain

_Required_: No

_Type_: List of <a href="resourcedomaindefinition.md">ResourceDomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetReferenceList

_Required_: No

_Type_: List of <a href="subnetreferencelistdefinition.md">SubnetReferenceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserReferenceList

_Required_: No

_Type_: List of <a href="userreferencelistdefinition.md">UserReferenceListDefinition</a>

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

#### IsDefault

Returns the <code>IsDefault</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### State

Returns the <code>State</code> value.

