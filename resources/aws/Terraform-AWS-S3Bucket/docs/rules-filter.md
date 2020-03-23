# Terraform::AWS::S3Bucket Rules Filter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="rules-filter-tags.md">Tags</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="rules-filter-tags.md">Tags</a></i>
</pre>

## Properties

#### Prefix

Object keyname prefix that identifies subset of objects to which the rule applies.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags that identifies subset of objects to which the rule applies.
The rule applies only to objects having all the tags in its tagset.

_Required_: No

_Type_: List of <a href="rules-filter-tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

