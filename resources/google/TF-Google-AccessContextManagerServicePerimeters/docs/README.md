# TF::Google::AccessContextManagerServicePerimeters

Replace all existing Service Perimeters in an Access Policy with the Service Perimeters provided. This is done atomically.
This is a bulk edit of all Service Perimeters and may override existing Service Perimeters created by `google_access_context_manager_service_perimeter`,
thus causing a permadiff if used alongside `google_access_context_manager_service_perimeter` on the same parent.


To get more information about ServicePerimeters, see:

* [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)
* How-to Guides
    * [Service Perimeter Quickstart](https://cloud.google.com/vpc-service-controls/docs/quickstart)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::AccessContextManagerServicePerimeters",
    "Properties" : {
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#serviceperimeters" title="ServicePerimeters">ServicePerimeters</a>" : <i>[ <a href="serviceperimetersdefinition.md">ServicePerimetersDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::AccessContextManagerServicePerimeters
Properties:
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#serviceperimeters" title="ServicePerimeters">ServicePerimeters</a>: <i>
      - <a href="serviceperimetersdefinition.md">ServicePerimetersDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Parent

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePerimeters

_Required_: No

_Type_: List of <a href="serviceperimetersdefinition.md">ServicePerimetersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

