# Terraform::Cloudflare::AccessPolicy Include

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#email" title="Email">Email</a>" : <i>[ String, ... ]</i>,
    "<a href="#emaildomain" title="EmailDomain">EmailDomain</a>" : <i>[ String, ... ]</i>,
    "<a href="#everyone" title="Everyone">Everyone</a>" : <i>Boolean</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#email" title="Email">Email</a>: <i>
      - String</i>
<a href="#emaildomain" title="EmailDomain">EmailDomain</a>: <i>
      - String</i>
<a href="#everyone" title="Everyone">Everyone</a>: <i>Boolean</i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - String</i>
</pre>

## Properties

#### Email

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailDomain

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Everyone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

