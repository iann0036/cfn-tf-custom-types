# Terraform::Google::AccessContextManagerServicePerimeterResource

Allows configuring a single GCP resource that should be inside of a service perimeter.
This resource is intended to be used in cases where it is not possible to compile a full list
of projects to include in a `google_access_context_manager_service_perimeter` resource,
to enable them to be added separately.

~> **Note:** If this resource is used alongside a `google_access_context_manager_service_perimeter` resource,
the service perimeter resource must have a `lifecycle` block with `ignore_changes = [status[0].resources]` so
they don't fight over which resources should be in the policy.


To get more information about ServicePerimeterResource, see:

* [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)
* How-to Guides
    * [Service Perimeter Quickstart](https://cloud.google.com/vpc-service-controls/docs/quickstart)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::AccessContextManagerServicePerimeterResource",
    "Properties" : {
        "<a href="#perimetername" title="PerimeterName">PerimeterName</a>" : <i>String</i>,
        "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::AccessContextManagerServicePerimeterResource
Properties:
    <a href="#perimetername" title="PerimeterName">PerimeterName</a>: <i>String</i>
    <a href="#resource" title="Resource">Resource</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### PerimeterName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resource

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

