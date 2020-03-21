# Terraform::OpenStack::IdentityUserV3 MultiFactorAuthRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rule" title="Rule">Rule</a>: <i>
      - String</i>
</pre>

## Properties

#### Rule

A list of authentication plugins that the user must
authenticate with.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

