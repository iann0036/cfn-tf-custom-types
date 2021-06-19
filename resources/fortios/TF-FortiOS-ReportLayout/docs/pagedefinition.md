# TF::FortiOS::ReportLayout PageDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columnbreakbefore" title="ColumnBreakBefore">ColumnBreakBefore</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>String</i>,
    "<a href="#pagebreakbefore" title="PageBreakBefore">PageBreakBefore</a>" : <i>String</i>,
    "<a href="#paper" title="Paper">Paper</a>" : <i>String</i>,
    "<a href="#footer" title="Footer">Footer</a>" : <i>[ <a href="footerdefinition.md">FooterDefinition</a>, ... ]</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="headerdefinition.md">HeaderDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#columnbreakbefore" title="ColumnBreakBefore">ColumnBreakBefore</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>String</i>
<a href="#pagebreakbefore" title="PageBreakBefore">PageBreakBefore</a>: <i>String</i>
<a href="#paper" title="Paper">Paper</a>: <i>String</i>
<a href="#footer" title="Footer">Footer</a>: <i>
      - <a href="footerdefinition.md">FooterDefinition</a></i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="headerdefinition.md">HeaderDefinition</a></i>
</pre>

## Properties

#### ColumnBreakBefore

Report page auto column break before heading. Valid values: `heading1`, `heading2`, `heading3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Report page options. Valid values: `header-on-first-page`, `footer-on-first-page`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PageBreakBefore

Report page auto page break before heading. Valid values: `heading1`, `heading2`, `heading3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paper

Report page paper. Valid values: `a4`, `letter`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Footer

_Required_: No

_Type_: List of <a href="footerdefinition.md">FooterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="headerdefinition.md">HeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

