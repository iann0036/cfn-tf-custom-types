# TF::Dynatrace::CalculatedServiceMetric ComparisonDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#negate" title="Negate">Negate</a>" : <i>Boolean</i>,
    "<a href="#boolean" title="Boolean">Boolean</a>" : <i>[ <a href="booleandefinition.md">BooleanDefinition</a>, ... ]</i>,
    "<a href="#esbinputnodetype" title="EsbInputNodeType">EsbInputNodeType</a>" : <i>[ <a href="esbinputnodetypedefinition.md">EsbInputNodeTypeDefinition</a>, ... ]</i>,
    "<a href="#failedstate" title="FailedState">FailedState</a>" : <i>[ <a href="failedstatedefinition.md">FailedStateDefinition</a>, ... ]</i>,
    "<a href="#failurereason" title="FailureReason">FailureReason</a>" : <i>[ <a href="failurereasondefinition.md">FailureReasonDefinition</a>, ... ]</i>,
    "<a href="#faststring" title="FastString">FastString</a>" : <i>[ <a href="faststringdefinition.md">FastStringDefinition</a>, ... ]</i>,
    "<a href="#flawstate" title="FlawState">FlawState</a>" : <i>[ <a href="flawstatedefinition.md">FlawStateDefinition</a>, ... ]</i>,
    "<a href="#generic" title="Generic">Generic</a>" : <i>[ <a href="genericdefinition.md">GenericDefinition</a>, ... ]</i>,
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>[ <a href="httpmethoddefinition.md">HttpMethodDefinition</a>, ... ]</i>,
    "<a href="#httpstatusclass" title="HttpStatusClass">HttpStatusClass</a>" : <i>[ <a href="httpstatusclassdefinition.md">HttpStatusClassDefinition</a>, ... ]</i>,
    "<a href="#iibinputnodetype" title="IibInputNodeType">IibInputNodeType</a>" : <i>[ <a href="iibinputnodetypedefinition.md">IibInputNodeTypeDefinition</a>, ... ]</i>,
    "<a href="#number" title="Number">Number</a>" : <i>[ <a href="numberdefinition.md">NumberDefinition</a>, ... ]</i>,
    "<a href="#numberrequestattribute" title="NumberRequestAttribute">NumberRequestAttribute</a>" : <i>[ <a href="numberrequestattributedefinition.md">NumberRequestAttributeDefinition</a>, ... ]</i>,
    "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>[ <a href="servicetypedefinition.md">ServiceTypeDefinition</a>, ... ]</i>,
    "<a href="#string" title="String">String</a>" : <i>[ <a href="stringdefinition.md">StringDefinition</a>, ... ]</i>,
    "<a href="#stringrequestattribute" title="StringRequestAttribute">StringRequestAttribute</a>" : <i>[ <a href="stringrequestattributedefinition.md">StringRequestAttributeDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>,
    "<a href="#zoscalltype" title="ZosCallType">ZosCallType</a>" : <i>[ <a href="zoscalltypedefinition.md">ZosCallTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#negate" title="Negate">Negate</a>: <i>Boolean</i>
<a href="#boolean" title="Boolean">Boolean</a>: <i>
      - <a href="booleandefinition.md">BooleanDefinition</a></i>
<a href="#esbinputnodetype" title="EsbInputNodeType">EsbInputNodeType</a>: <i>
      - <a href="esbinputnodetypedefinition.md">EsbInputNodeTypeDefinition</a></i>
<a href="#failedstate" title="FailedState">FailedState</a>: <i>
      - <a href="failedstatedefinition.md">FailedStateDefinition</a></i>
<a href="#failurereason" title="FailureReason">FailureReason</a>: <i>
      - <a href="failurereasondefinition.md">FailureReasonDefinition</a></i>
<a href="#faststring" title="FastString">FastString</a>: <i>
      - <a href="faststringdefinition.md">FastStringDefinition</a></i>
<a href="#flawstate" title="FlawState">FlawState</a>: <i>
      - <a href="flawstatedefinition.md">FlawStateDefinition</a></i>
<a href="#generic" title="Generic">Generic</a>: <i>
      - <a href="genericdefinition.md">GenericDefinition</a></i>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>
      - <a href="httpmethoddefinition.md">HttpMethodDefinition</a></i>
<a href="#httpstatusclass" title="HttpStatusClass">HttpStatusClass</a>: <i>
      - <a href="httpstatusclassdefinition.md">HttpStatusClassDefinition</a></i>
<a href="#iibinputnodetype" title="IibInputNodeType">IibInputNodeType</a>: <i>
      - <a href="iibinputnodetypedefinition.md">IibInputNodeTypeDefinition</a></i>
<a href="#number" title="Number">Number</a>: <i>
      - <a href="numberdefinition.md">NumberDefinition</a></i>
<a href="#numberrequestattribute" title="NumberRequestAttribute">NumberRequestAttribute</a>: <i>
      - <a href="numberrequestattributedefinition.md">NumberRequestAttributeDefinition</a></i>
<a href="#servicetype" title="ServiceType">ServiceType</a>: <i>
      - <a href="servicetypedefinition.md">ServiceTypeDefinition</a></i>
<a href="#string" title="String">String</a>: <i>
      - <a href="stringdefinition.md">StringDefinition</a></i>
<a href="#stringrequestattribute" title="StringRequestAttribute">StringRequestAttribute</a>: <i>
      - <a href="stringrequestattributedefinition.md">StringRequestAttributeDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
<a href="#zoscalltype" title="ZosCallType">ZosCallType</a>: <i>
      - <a href="zoscalltypedefinition.md">ZosCallTypeDefinition</a></i>
</pre>

## Properties

#### Negate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Boolean

_Required_: No

_Type_: List of <a href="booleandefinition.md">BooleanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EsbInputNodeType

_Required_: No

_Type_: List of <a href="esbinputnodetypedefinition.md">EsbInputNodeTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedState

_Required_: No

_Type_: List of <a href="failedstatedefinition.md">FailedStateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureReason

_Required_: No

_Type_: List of <a href="failurereasondefinition.md">FailureReasonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastString

_Required_: No

_Type_: List of <a href="faststringdefinition.md">FastStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlawState

_Required_: No

_Type_: List of <a href="flawstatedefinition.md">FlawStateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Generic

_Required_: No

_Type_: List of <a href="genericdefinition.md">GenericDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

_Required_: No

_Type_: List of <a href="httpmethoddefinition.md">HttpMethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpStatusClass

_Required_: No

_Type_: List of <a href="httpstatusclassdefinition.md">HttpStatusClassDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IibInputNodeType

_Required_: No

_Type_: List of <a href="iibinputnodetypedefinition.md">IibInputNodeTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Number

_Required_: No

_Type_: List of <a href="numberdefinition.md">NumberDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberRequestAttribute

_Required_: No

_Type_: List of <a href="numberrequestattributedefinition.md">NumberRequestAttributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

_Required_: No

_Type_: List of <a href="servicetypedefinition.md">ServiceTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### String

_Required_: No

_Type_: List of <a href="stringdefinition.md">StringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringRequestAttribute

_Required_: No

_Type_: List of <a href="stringrequestattributedefinition.md">StringRequestAttributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZosCallType

_Required_: No

_Type_: List of <a href="zoscalltypedefinition.md">ZosCallTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

