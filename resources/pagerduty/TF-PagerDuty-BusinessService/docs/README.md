# TF::PagerDuty::BusinessService

A [business service](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Business_Services/get_business_services) allows you to model capabilities that span multiple technical services and that may be owned by several different teams.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::BusinessService",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pointofcontact" title="PointOfContact">PointOfContact</a>" : <i>String</i>,
        "<a href="#team" title="Team">Team</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::BusinessService
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pointofcontact" title="PointOfContact">PointOfContact</a>: <i>String</i>
    <a href="#team" title="Team">Team</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Description

A human-friendly description of the service.
If not set, a placeholder of "Managed by Terraform" will be set.
* `point_of_contact` - (Optional) The owner of the business service.
* `type` - (Optional) Default value is `business_service`. Can also be set as `business_service_reference`.
* `team` - (Optional) ID of the team that owns the business service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the business service.
* `description` - (Optional) A human-friendly description of the service.
If not set, a placeholder of "Managed by Terraform" will be set.
* `point_of_contact` - (Optional) The owner of the business service.
* `type` - (Optional) Default value is `business_service`. Can also be set as `business_service_reference`.
* `team` - (Optional) ID of the team that owns the business service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PointOfContact

The owner of the business service.
* `type` - (Optional) Default value is `business_service`. Can also be set as `business_service_reference`.
* `team` - (Optional) ID of the team that owns the business service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Team

ID of the team that owns the business service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Default value is `business_service`. Can also be set as `business_service_reference`.
* `team` - (Optional) ID of the team that owns the business service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HtmlUrl

Returns the <code>HtmlUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### Self

Returns the <code>Self</code> value.

#### Summary

Returns the <code>Summary</code> value.

