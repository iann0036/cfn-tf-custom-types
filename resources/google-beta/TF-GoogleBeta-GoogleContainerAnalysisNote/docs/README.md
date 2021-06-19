# TF::GoogleBeta::GoogleContainerAnalysisNote

CloudFormation equivalent of google_container_analysis_note

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleContainerAnalysisNote",
    "Properties" : {
        "<a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>" : <i>String</i>,
        "<a href="#longdescription" title="LongDescription">LongDescription</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#relatednotenames" title="RelatedNoteNames">RelatedNoteNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#shortdescription" title="ShortDescription">ShortDescription</a>" : <i>String</i>,
        "<a href="#attestationauthority" title="AttestationAuthority">AttestationAuthority</a>" : <i>[ <a href="attestationauthoritydefinition.md">AttestationAuthorityDefinition</a>, ... ]</i>,
        "<a href="#relatedurl" title="RelatedUrl">RelatedUrl</a>" : <i>[ <a href="relatedurldefinition.md">RelatedUrlDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleContainerAnalysisNote
Properties:
    <a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>: <i>String</i>
    <a href="#longdescription" title="LongDescription">LongDescription</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#relatednotenames" title="RelatedNoteNames">RelatedNoteNames</a>: <i>
      - String</i>
    <a href="#shortdescription" title="ShortDescription">ShortDescription</a>: <i>String</i>
    <a href="#attestationauthority" title="AttestationAuthority">AttestationAuthority</a>: <i>
      - <a href="attestationauthoritydefinition.md">AttestationAuthorityDefinition</a></i>
    <a href="#relatedurl" title="RelatedUrl">RelatedUrl</a>: <i>
      - <a href="relatedurldefinition.md">RelatedUrlDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ExpirationTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelatedNoteNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttestationAuthority

_Required_: No

_Type_: List of <a href="attestationauthoritydefinition.md">AttestationAuthorityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelatedUrl

_Required_: No

_Type_: List of <a href="relatedurldefinition.md">RelatedUrlDefinition</a>

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Kind

Returns the <code>Kind</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

