# TF::AWS::LexBot

Provides an Amazon Lex Bot resource. For more information see
[Amazon Lex: How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LexBot",
    "Properties" : {
        "<a href="#childdirected" title="ChildDirected">ChildDirected</a>" : <i>Boolean</i>,
        "<a href="#createversion" title="CreateVersion">CreateVersion</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#detectsentiment" title="DetectSentiment">DetectSentiment</a>" : <i>Boolean</i>,
        "<a href="#enablemodelimprovements" title="EnableModelImprovements">EnableModelImprovements</a>" : <i>Boolean</i>,
        "<a href="#idlesessionttlinseconds" title="IdleSessionTtlInSeconds">IdleSessionTtlInSeconds</a>" : <i>Double</i>,
        "<a href="#locale" title="Locale">Locale</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nluintentconfidencethreshold" title="NluIntentConfidenceThreshold">NluIntentConfidenceThreshold</a>" : <i>Double</i>,
        "<a href="#processbehavior" title="ProcessBehavior">ProcessBehavior</a>" : <i>String</i>,
        "<a href="#voiceid" title="VoiceId">VoiceId</a>" : <i>String</i>,
        "<a href="#abortstatement" title="AbortStatement">AbortStatement</a>" : <i>[ <a href="abortstatementdefinition.md">AbortStatementDefinition</a>, ... ]</i>,
        "<a href="#clarificationprompt" title="ClarificationPrompt">ClarificationPrompt</a>" : <i>[ <a href="clarificationpromptdefinition.md">ClarificationPromptDefinition</a>, ... ]</i>,
        "<a href="#intent" title="Intent">Intent</a>" : <i>[ <a href="intentdefinition.md">IntentDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LexBot
Properties:
    <a href="#childdirected" title="ChildDirected">ChildDirected</a>: <i>Boolean</i>
    <a href="#createversion" title="CreateVersion">CreateVersion</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#detectsentiment" title="DetectSentiment">DetectSentiment</a>: <i>Boolean</i>
    <a href="#enablemodelimprovements" title="EnableModelImprovements">EnableModelImprovements</a>: <i>Boolean</i>
    <a href="#idlesessionttlinseconds" title="IdleSessionTtlInSeconds">IdleSessionTtlInSeconds</a>: <i>Double</i>
    <a href="#locale" title="Locale">Locale</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nluintentconfidencethreshold" title="NluIntentConfidenceThreshold">NluIntentConfidenceThreshold</a>: <i>Double</i>
    <a href="#processbehavior" title="ProcessBehavior">ProcessBehavior</a>: <i>String</i>
    <a href="#voiceid" title="VoiceId">VoiceId</a>: <i>String</i>
    <a href="#abortstatement" title="AbortStatement">AbortStatement</a>: <i>
      - <a href="abortstatementdefinition.md">AbortStatementDefinition</a></i>
    <a href="#clarificationprompt" title="ClarificationPrompt">ClarificationPrompt</a>: <i>
      - <a href="clarificationpromptdefinition.md">ClarificationPromptDefinition</a></i>
    <a href="#intent" title="Intent">Intent</a>: <i>
      - <a href="intentdefinition.md">IntentDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ChildDirected

By specifying true, you confirm that your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. For more information see the [Amazon Lex FAQ](https://aws.amazon.com/lex/faqs#data-security) and the [Amazon Lex PutBot API Docs](https://docs.aws.amazon.com/lex/latest/dg/API_PutBot.html#lex-PutBot-request-childDirected).

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVersion

Determines if a new bot version is created when the initial resource is created and on each update. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the bot. Must be less than or equal to 200 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectSentiment

When set to true user utterances are sent to Amazon Comprehend for sentiment analysis. If you don't specify detectSentiment, the default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableModelImprovements

Set to `true` to enable access to natural language understanding improvements. When you set the `enable_model_improvements` parameter to true you can use the `nlu_intent_confidence_threshold` parameter to configure confidence scores. For more information, see [Confidence Scores](https://docs.aws.amazon.com/lex/latest/dg/confidence-scores.html). You can only set the `enable_model_improvements` parameter in certain Regions. If you set the parameter to true, your bot has access to accuracy improvements. For more information see the [Amazon Lex Bot PutBot API Docs](https://docs.aws.amazon.com/lex/latest/dg/API_PutBot.html#lex-PutBot-request-enableModelImprovements).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleSessionTtlInSeconds

The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. Default is `300`. Must be a number between 60 and 86400 (inclusive).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locale

Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot. For available locales, see [Amazon Lex Bot PutBot API Docs](https://docs.aws.amazon.com/lex/latest/dg/API_PutBot.html#lex-PutBot-request-locale). Default is `en-US`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the bot that you want to create, case sensitive. Must be between 2 and 50 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NluIntentConfidenceThreshold

Determines the threshold where Amazon Lex will insert the AMAZON.FallbackIntent, AMAZON.KendraSearchIntent, or both when returning alternative intents in a PostContent or PostText response. AMAZON.FallbackIntent and AMAZON.KendraSearchIntent are only inserted if they are configured for the bot. For more information see [Amazon Lex Bot PutBot API Docs](https://docs.aws.amazon.com/lex/latest/dg/API_PutBot.html#lex-PutBot-request-nluIntentConfidenceThreshold) This value requires `enable_model_improvements` to be set to `true` and the default is `0`. Must be a float between 0 and 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessBehavior

If you set the `process_behavior` element to `BUILD`, Amazon Lex builds the bot so that it can be run. If you set the element to `SAVE` Amazon Lex saves the bot, but doesn't build it. Default is `SAVE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoiceId

The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see [Available Voices](http://docs.aws.amazon.com/polly/latest/dg/voicelist.html) in the Amazon Polly Developer Guide.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AbortStatement

_Required_: No

_Type_: List of <a href="abortstatementdefinition.md">AbortStatementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClarificationPrompt

_Required_: No

_Type_: List of <a href="clarificationpromptdefinition.md">ClarificationPromptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Intent

_Required_: No

_Type_: List of <a href="intentdefinition.md">IntentDefinition</a>

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

#### FailureReason

Returns the <code>FailureReason</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdatedDate

Returns the <code>LastUpdatedDate</code> value.

#### Status

Returns the <code>Status</code> value.

#### Version

Returns the <code>Version</code> value.

