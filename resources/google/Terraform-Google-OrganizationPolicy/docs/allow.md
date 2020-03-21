# Terraform::Google::OrganizationPolicy Allow

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#all" title="All">All</a>" : <i>Boolean</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#all" title="All">All</a>: <i>Boolean</i>
<a href="#values" title="Values">Values</a>: <i>
      - String</i>
</pre>

## Properties

#### All

The policy allows or denies all values.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

The policy can define specific values that are allowed or denied.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

