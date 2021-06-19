# TF::Volterra::VirtualHost AuthHmacDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#primkeyexpiry" title="PrimKeyExpiry">PrimKeyExpiry</a>" : <i>String</i>,
    "<a href="#seckeyexpiry" title="SecKeyExpiry">SecKeyExpiry</a>" : <i>String</i>,
    "<a href="#primkey" title="PrimKey">PrimKey</a>" : <i>[ <a href="primkeydefinition.md">PrimKeyDefinition</a>, ... ]</i>,
    "<a href="#seckey" title="SecKey">SecKey</a>" : <i>[ <a href="seckeydefinition.md">SecKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#primkeyexpiry" title="PrimKeyExpiry">PrimKeyExpiry</a>: <i>String</i>
<a href="#seckeyexpiry" title="SecKeyExpiry">SecKeyExpiry</a>: <i>String</i>
<a href="#primkey" title="PrimKey">PrimKey</a>: <i>
      - <a href="primkeydefinition.md">PrimKeyDefinition</a></i>
<a href="#seckey" title="SecKey">SecKey</a>: <i>
      - <a href="seckeydefinition.md">SecKeyDefinition</a></i>
</pre>

## Properties

#### PrimKeyExpiry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecKeyExpiry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimKey

_Required_: No

_Type_: List of <a href="primkeydefinition.md">PrimKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecKey

_Required_: No

_Type_: List of <a href="seckeydefinition.md">SecKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

