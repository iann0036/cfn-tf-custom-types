# TF::Google::BinaryAuthorizationAttestor AttestationAuthorityNoteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#notereference" title="NoteReference">NoteReference</a>" : <i>String</i>,
    "<a href="#publickeys" title="PublicKeys">PublicKeys</a>" : <i>[ <a href="publickeysdefinition.md">PublicKeysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#notereference" title="NoteReference">NoteReference</a>: <i>String</i>
<a href="#publickeys" title="PublicKeys">PublicKeys</a>: <i>
      - <a href="publickeysdefinition.md">PublicKeysDefinition</a></i>
</pre>

## Properties

#### NoteReference

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeys

_Required_: No

_Type_: List of <a href="publickeysdefinition.md">PublicKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

