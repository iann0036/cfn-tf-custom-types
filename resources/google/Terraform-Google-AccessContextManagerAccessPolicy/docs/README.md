# Terraform::Google::AccessContextManagerAccessPolicy

AccessPolicy is a container for AccessLevels (which define the necessary
attributes to use GCP services) and ServicePerimeters (which define
regions of services able to freely pass data within a perimeter). An
access policy is globally visible within an organization, and the
restrictions it specifies apply to all projects within an organization.


To get more information about AccessPolicy, see:

* [API documentation](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies)
* How-to Guides
    * [Access Policy Quickstart](https://cloud.google.com/access-context-manager/docs/quickstart)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::AccessContextManagerAccessPolicy",
    "Properties" : {
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::AccessContextManagerAccessPolicy
Properties:
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Parent

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

