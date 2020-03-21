# Terraform::AzureRM::EventgridEventSubscription SubjectFilter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>" : <i>Boolean</i>,
    "<a href="#subjectbeginswith" title="SubjectBeginsWith">SubjectBeginsWith</a>" : <i>String</i>,
    "<a href="#subjectendswith" title="SubjectEndsWith">SubjectEndsWith</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#casesensitive" title="CaseSensitive">CaseSensitive</a>: <i>Boolean</i>
<a href="#subjectbeginswith" title="SubjectBeginsWith">SubjectBeginsWith</a>: <i>String</i>
<a href="#subjectendswith" title="SubjectEndsWith">SubjectEndsWith</a>: <i>String</i>
</pre>

## Properties

#### CaseSensitive

Specifies if `subject_begins_with` and `subject_ends_with` case sensitive. This value defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectBeginsWith

A string to filter events for an event subscription based on a resource path prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectEndsWith

A string to filter events for an event subscription based on a resource path suffix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

