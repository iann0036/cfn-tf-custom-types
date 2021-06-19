# TF::Cloudflare::WorkerScript

Provides a Cloudflare worker script resource. In order for a script to be active, you'll also need to setup a `cloudflare_worker_route`. *NOTE:*  This resource uses the Cloudflare account APIs. This requires setting the `CLOUDFLARE_ACCOUNT_ID` environment variable or `account_id` provider argument.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::WorkerScript",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#kvnamespacebinding" title="KvNamespaceBinding">KvNamespaceBinding</a>" : <i>[ <a href="kvnamespacebindingdefinition.md">KvNamespaceBindingDefinition</a>, ... ]</i>,
        "<a href="#plaintextbinding" title="PlainTextBinding">PlainTextBinding</a>" : <i>[ <a href="plaintextbindingdefinition.md">PlainTextBindingDefinition</a>, ... ]</i>,
        "<a href="#secrettextbinding" title="SecretTextBinding">SecretTextBinding</a>" : <i>[ <a href="secrettextbindingdefinition.md">SecretTextBindingDefinition</a>, ... ]</i>,
        "<a href="#webassemblybinding" title="WebassemblyBinding">WebassemblyBinding</a>" : <i>[ <a href="webassemblybindingdefinition.md">WebassemblyBindingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::WorkerScript
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#kvnamespacebinding" title="KvNamespaceBinding">KvNamespaceBinding</a>: <i>
      - <a href="kvnamespacebindingdefinition.md">KvNamespaceBindingDefinition</a></i>
    <a href="#plaintextbinding" title="PlainTextBinding">PlainTextBinding</a>: <i>
      - <a href="plaintextbindingdefinition.md">PlainTextBindingDefinition</a></i>
    <a href="#secrettextbinding" title="SecretTextBinding">SecretTextBinding</a>: <i>
      - <a href="secrettextbindingdefinition.md">SecretTextBindingDefinition</a></i>
    <a href="#webassemblybinding" title="WebassemblyBinding">WebassemblyBinding</a>: <i>
      - <a href="webassemblybindingdefinition.md">WebassemblyBindingDefinition</a></i>
</pre>

## Properties

#### Content

The script content.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The global variable for the binding in your Worker code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KvNamespaceBinding

_Required_: No

_Type_: List of <a href="kvnamespacebindingdefinition.md">KvNamespaceBindingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlainTextBinding

_Required_: No

_Type_: List of <a href="plaintextbindingdefinition.md">PlainTextBindingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretTextBinding

_Required_: No

_Type_: List of <a href="secrettextbindingdefinition.md">SecretTextBindingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebassemblyBinding

_Required_: No

_Type_: List of <a href="webassemblybindingdefinition.md">WebassemblyBindingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

