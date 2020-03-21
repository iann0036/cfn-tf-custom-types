# Terraform::OpenTelekomCloud::WafPreciseprotectionRuleV1 Conditions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#contents" title="Contents">Contents</a>" : <i>[ String, ... ]</i>,
    "<a href="#index" title="Index">Index</a>" : <i>String</i>,
    "<a href="#logic" title="Logic">Logic</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#contents" title="Contents">Contents</a>: <i>
      - String</i>
<a href="#index" title="Index">Index</a>: <i>String</i>
<a href="#logic" title="Logic">Logic</a>: <i>Double</i>
</pre>

## Properties

#### Category

Specifies the condition type. The value can be url, user-agent, ip, params, cookie, referer, or header.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contents

Specifies a list of content matching the condition. Currently, only one value is accepted.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

If `category` is set to cookie, index indicates cookie name, if set to params, index indicates param name,
if set to header, index indicates an option in the header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logic

1,2,3,4,5,6,7, and 8 indicate include, exclude, equal to, not equal to, prefix is, prefix is not, suffix is,
and suffix is not, respectively. If `category` is set to ip, logic can only be 3 or 4.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

