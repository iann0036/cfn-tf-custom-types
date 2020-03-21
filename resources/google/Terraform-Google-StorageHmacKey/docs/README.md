# Terraform::Google::StorageHmacKey

The hmacKeys resource represents an HMAC key within Cloud Storage. The resource
consists of a secret and HMAC key metadata. HMAC keys can be used as credentials
for service accounts.


To get more information about HmacKey, see:

* [API documentation](https://cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/storage/docs/authentication/managing-hmackeys)

~> **Warning:** All arguments including the `secret` value will be stored in the raw
state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).
On import, the `secret` value will not be retrieved.

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=storage_hmac_key&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageHmacKey",
    "Properties" : {
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageHmacKey
Properties:
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#serviceaccountemail" title="ServiceAccountEmail">ServiceAccountEmail</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountEmail

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessId

Returns the <code>AccessId</code> value.

#### Secret

Returns the <code>Secret</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### Updated

Returns the <code>Updated</code> value.

