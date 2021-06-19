# TF::AzureRM::StorageAccount PrivateLinkAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endpointresourceid" title="EndpointResourceId">EndpointResourceId</a>" : <i>String</i>,
    "<a href="#endpointtenantid" title="EndpointTenantId">EndpointTenantId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#endpointresourceid" title="EndpointResourceId">EndpointResourceId</a>: <i>String</i>
<a href="#endpointtenantid" title="EndpointTenantId">EndpointTenantId</a>: <i>String</i>
</pre>

## Properties

#### EndpointResourceId

The resource id of the resource access rule to be granted access.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointTenantId

The tenant id of the resource of the resource access rule to be granted access. Defaults to the current tenant id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

