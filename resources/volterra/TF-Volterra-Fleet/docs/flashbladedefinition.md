# TF::Volterra::Fleet FlashBladeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enablesnapshotdirectory" title="EnableSnapshotDirectory">EnableSnapshotDirectory</a>" : <i>Boolean</i>,
    "<a href="#exportrules" title="ExportRules">ExportRules</a>" : <i>String</i>,
    "<a href="#flashblades" title="FlashBlades">FlashBlades</a>" : <i>[ <a href="flashbladesdefinition.md">FlashBladesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enablesnapshotdirectory" title="EnableSnapshotDirectory">EnableSnapshotDirectory</a>: <i>Boolean</i>
<a href="#exportrules" title="ExportRules">ExportRules</a>: <i>String</i>
<a href="#flashblades" title="FlashBlades">FlashBlades</a>: <i>
      - <a href="flashbladesdefinition.md">FlashBladesDefinition</a></i>
</pre>

## Properties

#### EnableSnapshotDirectory

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportRules

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlashBlades

_Required_: No

_Type_: List of <a href="flashbladesdefinition.md">FlashBladesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

