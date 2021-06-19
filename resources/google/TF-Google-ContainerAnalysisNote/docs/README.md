# TF::Google::ContainerAnalysisNote

A Container Analysis note is a high-level piece of metadata that
describes a type of analysis that can be done for a resource.


To get more information about Note, see:

* [API documentation](https://cloud.google.com/container-analysis/api/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/container-analysis/)
    * [Creating Attestations (Occurrences)](https://cloud.google.com/binary-authorization/docs/making-attestations)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=container_analysis_note_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ContainerAnalysisNote",
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
Type: TF::Google::ContainerAnalysisNote
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

