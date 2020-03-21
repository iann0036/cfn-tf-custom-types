# Terraform::Fastly::ServiceV1 Dictionary

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#writeonly" title="WriteOnly">WriteOnly</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#writeonly" title="WriteOnly">WriteOnly</a>: <i>Boolean</i>
</pre>

## Properties

#### Name

A unique name to identify this dictionary.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteOnly

If `true`, the dictionary is a private dictionary, and items are not readable in the UI or
via API. Default is `false`. It is important to note that changing this attribute will delete and recreate the
dictionary, discard the current items in the dictionary. Using a write-only/private dictionary should only be done if
the items are managed outside of Terraform.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

