# TF::AVI::Authprofile TacacsPlusDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#server" title="Server">Server</a>" : <i>[ String, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>,
    "<a href="#authorizationattrs" title="AuthorizationAttrs">AuthorizationAttrs</a>" : <i>[ <a href="authorizationattrsdefinition.md">AuthorizationAttrsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#server" title="Server">Server</a>: <i>
      - String</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
<a href="#authorizationattrs" title="AuthorizationAttrs">AuthorizationAttrs</a>: <i>
      - <a href="authorizationattrsdefinition.md">AuthorizationAttrsDefinition</a></i>
</pre>

## Properties

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationAttrs

_Required_: No

_Type_: List of <a href="authorizationattrsdefinition.md">AuthorizationAttrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

