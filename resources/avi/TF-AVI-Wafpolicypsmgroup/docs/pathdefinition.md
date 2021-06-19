# TF::AVI::Wafpolicypsmgroup PathDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchcase" title="MatchCase">MatchCase</a>" : <i>String</i>,
    "<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>" : <i>String</i>,
    "<a href="#matchstr" title="MatchStr">MatchStr</a>" : <i>[ String, ... ]</i>,
    "<a href="#stringgrouprefs" title="StringGroupRefs">StringGroupRefs</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchcase" title="MatchCase">MatchCase</a>: <i>String</i>
<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>: <i>String</i>
<a href="#matchstr" title="MatchStr">MatchStr</a>: <i>
      - String</i>
<a href="#stringgrouprefs" title="StringGroupRefs">StringGroupRefs</a>: <i>
      - String</i>
</pre>

## Properties

#### MatchCase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCriteria

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchStr

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringGroupRefs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

