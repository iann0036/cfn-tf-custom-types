# TF::AWS::LexIntent

Provides an Amazon Lex Intent resource. For more information see
[Amazon Lex: How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LexIntent",
    "Properties" : {
        "<a href="#createversion" title="CreateVersion">CreateVersion</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentintentsignature" title="ParentIntentSignature">ParentIntentSignature</a>" : <i>String</i>,
        "<a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>" : <i>[ String, ... ]</i>,
        "<a href="#conclusionstatement" title="ConclusionStatement">ConclusionStatement</a>" : <i>[ <a href="conclusionstatementdefinition.md">ConclusionStatementDefinition</a>, ... ]</i>,
        "<a href="#confirmationprompt" title="ConfirmationPrompt">ConfirmationPrompt</a>" : <i>[ <a href="confirmationpromptdefinition.md">ConfirmationPromptDefinition</a>, ... ]</i>,
        "<a href="#dialogcodehook" title="DialogCodeHook">DialogCodeHook</a>" : <i>[ <a href="dialogcodehookdefinition.md">DialogCodeHookDefinition</a>, ... ]</i>,
        "<a href="#followupprompt" title="FollowUpPrompt">FollowUpPrompt</a>" : <i>[ <a href="followuppromptdefinition.md">FollowUpPromptDefinition</a>, ... ]</i>,
        "<a href="#fulfillmentactivity" title="FulfillmentActivity">FulfillmentActivity</a>" : <i>[ <a href="fulfillmentactivitydefinition.md">FulfillmentActivityDefinition</a>, ... ]</i>,
        "<a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>" : <i>[ <a href="rejectionstatementdefinition.md">RejectionStatementDefinition</a>, ... ]</i>,
        "<a href="#slot" title="Slot">Slot</a>" : <i>[ <a href="slotdefinition.md">SlotDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LexIntent
Properties:
    <a href="#createversion" title="CreateVersion">CreateVersion</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentintentsignature" title="ParentIntentSignature">ParentIntentSignature</a>: <i>String</i>
    <a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>: <i>
      - String</i>
    <a href="#conclusionstatement" title="ConclusionStatement">ConclusionStatement</a>: <i>
      - <a href="conclusionstatementdefinition.md">ConclusionStatementDefinition</a></i>
    <a href="#confirmationprompt" title="ConfirmationPrompt">ConfirmationPrompt</a>: <i>
      - <a href="confirmationpromptdefinition.md">ConfirmationPromptDefinition</a></i>
    <a href="#dialogcodehook" title="DialogCodeHook">DialogCodeHook</a>: <i>
      - <a href="dialogcodehookdefinition.md">DialogCodeHookDefinition</a></i>
    <a href="#followupprompt" title="FollowUpPrompt">FollowUpPrompt</a>: <i>
      - <a href="followuppromptdefinition.md">FollowUpPromptDefinition</a></i>
    <a href="#fulfillmentactivity" title="FulfillmentActivity">FulfillmentActivity</a>: <i>
      - <a href="fulfillmentactivitydefinition.md">FulfillmentActivityDefinition</a></i>
    <a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>: <i>
      - <a href="rejectionstatementdefinition.md">RejectionStatementDefinition</a></i>
    <a href="#slot" title="Slot">Slot</a>: <i>
      - <a href="slotdefinition.md">SlotDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CreateVersion

Determines if a new slot type version is created when the initial
resource is created and on each update. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the intent. Must be less than or equal to 200 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the intent, not case sensitive. Must be less than or equal to 100 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentIntentSignature

A unique identifier for the built-in intent to base this
intent on. To find the signature for an intent, see
[Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents)
in the Alexa Skills Kit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleUtterances

An array of utterances (strings) that a user might say to signal
the intent. For example, "I want {PizzaSize} pizza", "Order {Quantity} {PizzaSize} pizzas".
In each utterance, a slot name is enclosed in curly braces. Must have between 1 and 10 items in the list, and each item must be less than or equal to 200 characters in length.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConclusionStatement

_Required_: No

_Type_: List of <a href="conclusionstatementdefinition.md">ConclusionStatementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfirmationPrompt

_Required_: No

_Type_: List of <a href="confirmationpromptdefinition.md">ConfirmationPromptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DialogCodeHook

_Required_: No

_Type_: List of <a href="dialogcodehookdefinition.md">DialogCodeHookDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowUpPrompt

_Required_: No

_Type_: List of <a href="followuppromptdefinition.md">FollowUpPromptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FulfillmentActivity

_Required_: No

_Type_: List of <a href="fulfillmentactivitydefinition.md">FulfillmentActivityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectionStatement

_Required_: No

_Type_: List of <a href="rejectionstatementdefinition.md">RejectionStatementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot

_Required_: No

_Type_: List of <a href="slotdefinition.md">SlotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Checksum

Returns the <code>Checksum</code> value.

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdatedDate

Returns the <code>LastUpdatedDate</code> value.

#### Version

Returns the <code>Version</code> value.

