# TF::AzureRM::KubernetesCluster KubeletIdentityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#objectid" title="ObjectId">ObjectId</a>" : <i>String</i>,
    "<a href="#userassignedidentityid" title="UserAssignedIdentityId">UserAssignedIdentityId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#objectid" title="ObjectId">ObjectId</a>: <i>String</i>
<a href="#userassignedidentityid" title="UserAssignedIdentityId">UserAssignedIdentityId</a>: <i>String</i>
</pre>

## Properties

#### ClientId

The Client ID of the user-defined Managed Identity to be assigned to the Kubelets. If not specified a Managed Identity is created automatically.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectId

The Object ID of the user-defined Managed Identity assigned to the Kubelets.If not specified a Managed Identity is created automatically.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAssignedIdentityId

The ID of the User Assigned Identity assigned to the Kubelets. If not specified a Managed Identity is created automatically.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

