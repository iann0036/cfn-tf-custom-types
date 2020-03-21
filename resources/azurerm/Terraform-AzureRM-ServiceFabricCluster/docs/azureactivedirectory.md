# Terraform::AzureRM::ServiceFabricCluster AzureActiveDirectory

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientapplicationid" title="ClientApplicationId">ClientApplicationId</a>" : <i>String</i>,
    "<a href="#clusterapplicationid" title="ClusterApplicationId">ClusterApplicationId</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clientapplicationid" title="ClientApplicationId">ClientApplicationId</a>: <i>String</i>
<a href="#clusterapplicationid" title="ClusterApplicationId">ClusterApplicationId</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
</pre>

## Properties

#### ClientApplicationId

The Azure Active Directory Client ID which should be used for the Client Application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterApplicationId

The Azure Active Directory Cluster Application ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The Azure Active Directory Tenant ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

