# TF::VRA7::Deployment

Provides a VMware vRA7 deployment resource. This can be used to deploy vRA7 catalog items.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA7::Deployment",
    "Properties" : {
        "<a href="#businessgroupid" title="BusinessgroupId">BusinessgroupId</a>" : <i>String</i>,
        "<a href="#businessgroupname" title="BusinessgroupName">BusinessgroupName</a>" : <i>String</i>,
        "<a href="#catalogitemid" title="CatalogItemId">CatalogItemId</a>" : <i>String</i>,
        "<a href="#catalogitemname" title="CatalogItemName">CatalogItemName</a>" : <i>String</i>,
        "<a href="#deploymentconfiguration" title="DeploymentConfiguration">DeploymentConfiguration</a>" : <i>[ <a href="deploymentconfigurationdefinition.md">DeploymentConfigurationDefinition</a>, ... ]</i>,
        "<a href="#deploymentdestroy" title="DeploymentDestroy">DeploymentDestroy</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expirydate" title="ExpiryDate">ExpiryDate</a>" : <i>String</i>,
        "<a href="#leasedays" title="LeaseDays">LeaseDays</a>" : <i>Double</i>,
        "<a href="#reasons" title="Reasons">Reasons</a>" : <i>String</i>,
        "<a href="#waittimeout" title="WaitTimeout">WaitTimeout</a>" : <i>Double</i>,
        "<a href="#resourceconfiguration" title="ResourceConfiguration">ResourceConfiguration</a>" : <i>[ <a href="resourceconfigurationdefinition.md">ResourceConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA7::Deployment
Properties:
    <a href="#businessgroupid" title="BusinessgroupId">BusinessgroupId</a>: <i>String</i>
    <a href="#businessgroupname" title="BusinessgroupName">BusinessgroupName</a>: <i>String</i>
    <a href="#catalogitemid" title="CatalogItemId">CatalogItemId</a>: <i>String</i>
    <a href="#catalogitemname" title="CatalogItemName">CatalogItemName</a>: <i>String</i>
    <a href="#deploymentconfiguration" title="DeploymentConfiguration">DeploymentConfiguration</a>: <i>
      - <a href="deploymentconfigurationdefinition.md">DeploymentConfigurationDefinition</a></i>
    <a href="#deploymentdestroy" title="DeploymentDestroy">DeploymentDestroy</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expirydate" title="ExpiryDate">ExpiryDate</a>: <i>String</i>
    <a href="#leasedays" title="LeaseDays">LeaseDays</a>: <i>Double</i>
    <a href="#reasons" title="Reasons">Reasons</a>: <i>String</i>
    <a href="#waittimeout" title="WaitTimeout">WaitTimeout</a>: <i>Double</i>
    <a href="#resourceconfiguration" title="ResourceConfiguration">ResourceConfiguration</a>: <i>
      - <a href="resourceconfigurationdefinition.md">ResourceConfigurationDefinition</a></i>
</pre>

## Properties

#### BusinessgroupId

The id of the vRA business group to use for this deployment. Either businessgroup_id or businessgroup_name is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BusinessgroupName

The name of the vRA business group to use for this deployment. Either businessgroup_id or businessgroup_name is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogItemId

The id of the catalog item to deploy into vRA. Either catalog_item_id or catalog_item_name is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogItemName

The name of the catalog item to deploy into vRA. Either catalog_item_id or catalog_item_name is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentConfiguration

The configuration of the deployment from the catalog item. All blueprint custom properties including property groups can be added to this block. This property is discussed in detail below.

_Required_: No

_Type_: List of <a href="deploymentconfigurationdefinition.md">DeploymentConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiryDate

The date when the deployment will expire. To change lease, modify this field in main.tf. It has to be in the same format as in the state file. For e.g., "2020-11-25T20:29:37.845Z".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseDays

Number of lease days remaining for the deployment. NOTE: If this is not provided, the default lease_days in the catalog item will be configured. lease_days 0 means the lease never expires.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reasons

Reasons for requesting the deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitTimeout

Wait time out for the request. If the request is not completed within the timeout period, do a terraform refresh later to check the status of the request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceConfiguration

_Required_: No

_Type_: List of <a href="resourceconfigurationdefinition.md">ResourceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### DeploymentId

Returns the <code>DeploymentId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### Owners

Returns the <code>Owners</code> value.

#### RequestStatus

Returns the <code>RequestStatus</code> value.

